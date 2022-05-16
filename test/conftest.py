from asyncio.log import logger
import os
import pytest

try:
    from test.temp_env_var import TEMP_ENV_VARS
except ImportError:
    logger.error("error ----")
    TEMP_ENV_VARS = {}
    ENV_VARS_TO_SUSPEND = []


@pytest.fixture(scope="session", autouse=True)
def tests_setup_and_teardown():
    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_ENV_VARS)
    print("initialized")
    # for env_var in TEMP_ENV_VARS:
        # print(env_var,TEMP_ENV_VARS[env_var])
        # os.environ[env_var]=TEMP_ENV_VARS[env_var]
    # os.environ["AWS_DEFAULT_REGION"]="us-east-1"
    yield
    # Will be executed after the last test
    os.environ.clear()
    os.environ.update(old_environ)
    