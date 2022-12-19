"""
End to end integration tests for the tap.
"""
import pytest
from integrations_testing_framework import *

import tap_pipedrive.cli as tap_pipedrive

# Config file
CONFIG_FILE = 'config.json'
# Streams file
STREAMS_FILE = 'tests/all-streams.json'
# Directories
CONFIGS_DIR = 'tests/configs/'
REQUESTS_DIR = 'tests/requests/'
RESPONSES_DIR = 'tests/responses/'
RECORDING_CONF = {
    'filter_req_data': ['api_token'],
}


@write_stdout(STREAMS_FILE)
@intercept_requests(os.path.join(REQUESTS_DIR, 'discovery.txt'), generate=True, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--discover'])
def test_discovery():
    """
    Test tap discover function.
    """
    tap_pipedrive.main()


@write_stdout(os.path.join(RESPONSES_DIR, 'activity_types.txt'))
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'activity_types.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'activity_types.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'activity_types',
                                                                          stream_key='stream')])
def test_activity_types():
    """
    Test stream 'activity_types'.
    """
    tap_pipedrive.main()


@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'currency.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'currency.txt'), generate=False)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'currency',
                                                                          stream_key='stream')])
def test_currency():
    """
    Test stream 'currency'.
    """
    tap_pipedrive.main()

@write_stdout(os.path.join(RESPONSES_DIR, 'deal_products.txt'))
@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'deal_products.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'deal_products.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'deal_products',
                                                                          stream_key='stream')])
def test_deal_products():
    """
    Test stream 'deal_products'
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'dealflow.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'dealflow.txt'), generate=False)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'dealflow',
                                                                          stream_key='stream')])
def test_dealflow():
    """
    Test stream 'dealflow'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'deals_summary.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'deals_summary.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'deals_summary',
                                                                          stream_key='stream')])
def test_deals_summary():
    """
    Test stream 'deals_summary'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'filters.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'filters.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'filters',
                                                                          stream_key='stream')])
def test_filters():
    """
    Test stream 'filters'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'pipelines.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'pipelines.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'pipelines',
                                                                          stream_key='stream')])
def test_pipelines():
    """
    Test stream 'pipelines'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'stages.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'stages.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'stages',
                                                                          stream_key='stream')])
def test_stages():
    """
    Test stream 'stages'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'activities.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'activities.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'activities',
                                                                          stream_key='stream')])
def test_activities():
    """
    Test stream 'activities'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'deal_details.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'deal_details.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'deal_details',
                                                                          stream_key='stream')])
def test_deal_details():
    """
    Test stream 'deal_details'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'deals.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'deals.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'deals',
                                                                          stream_key='stream')])
def test_deals():
    """
    Test stream 'deals'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'notes.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'notes.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'notes',
                                                                          stream_key='stream')])
def test_notes():
    """
    Test stream 'notes'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'organizations.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'organizations.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'organizations',
                                                                          stream_key='stream')])
def test_organizations():
    """
    Test stream 'organizations'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'persons.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'persons.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'persons',
                                                                          stream_key='stream')])
def test_persons():
    """
    Test stream 'persons'.
    """
    tap_pipedrive.main()

@assert_stdout_matches(os.path.join(RESPONSES_DIR, 'products.txt'))
@intercept_requests(os.path.join(REQUESTS_DIR, 'products.txt'), generate=False, **RECORDING_CONF)
@with_sys_args(['--config', CONFIG_FILE, '--properties', utils.select_schema(STREAMS_FILE,
                                                                          'products',
                                                                          stream_key='stream')])
def test_products():
    """
    Test stream 'products'.
    """
    tap_pipedrive.main()