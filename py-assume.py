import boto3
import os
import configparser
import sys

def assume(home_path, account_id, role_name):

    config = configparser.RawConfigParser()
    config.read(home_path + '/.aws/credentials')
    access_key = config['default']['aws_access_key_id']
    secret_access_key = config['default']['aws_secret_access_key']

    roleArn = 'arn:aws:iam::' + account_id + ':role/' + role_name

    sts_conn = boto3.client(
        'sts',
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_access_key
        )
    acct_b = sts_conn.assume_role(
        RoleArn=roleArn,
        RoleSessionName='AWSCLI-Session'
    )

    ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
    SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
    SESSION_TOKEN = acct_b['Credentials']['SessionToken']
    print ('access_key: %s \nsecret_key: %s \nsession_key: %s \n' % (ACCESS_KEY, SECRET_KEY, SESSION_TOKEN))

    section = 'assume'
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, 'aws_access_key_id', ACCESS_KEY)
    config.set(section, 'aws_secret_access_key', SECRET_KEY)
    config.set(section, 'aws_session_token', SESSION_TOKEN)

    try:
        with open(home_path + '/.aws/credentials', 'w') as file:
            config.write(file)
    except:
        print(e)
        sys.exit(1)

    print ('\nAdded or updated [assume] profile of ~/.aws/credentials with above assume key. Let\'s change profile to assume by below command.')
    print ('$ export AWS_DEFAULT_PROFILE=assume')

if __name__ == '__main__':
    # argv[1]: account_id, argv[2]: role name
    home_path = os.path.expanduser("~")
    if len(sys.argv)!=3:
        print('Error: Invalid parameters', file=sys.stderr)
        sys.exit(1)
    assume(home_path, sys.argv[1], sys.argv[2])