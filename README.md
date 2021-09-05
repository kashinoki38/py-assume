# py-assume

This is a simple python tool for configuring assume aws session key.  
This tool mechanesm are following.

- read session key from `~/.aws/config/credentials` 
- call sts.assume_role api and get assume session key
- update or add [assume] profile to `~/.aws/config/credentials` with assume keys 


## How to use

You must put 2 parameters as below.
```bash
$ python3 py-assume.py <aws account id> <role name to assume>
```

After execute `py-assume.py`, you need to change profile to `assume` by using like below command.

```bash
$ export AWS_DEFAULT_PROFILE=assume
```

### e.g. updated ~/.aws/credentials
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXX
aws_secret_access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[assume]
aws_access_key_id = YYYYYYYYYYYYYYYYYYYYYYY
aws_secret_access_key = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
aws_session_token = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

## TODO
- automatic profile change (by changing `AWS_DEFAULT_PROFILE`)
- selecting profile function