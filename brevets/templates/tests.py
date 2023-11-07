"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

{{disclaimer_text}}

#imports for what we need to test
import arrow
from acp_times import open_time, close_time

#helper functions to make test cases shorter to write
def format_time(time):
    return time.format('YYYY-MM-DDTHH:mm')

def assert_equal(actual, expected, msg = "unknown"):
    assert actual == expected, "Expected: " + str(expected) + " but got " + str(actual) + " at " + msg

def assert_time_equal(actual, expected, msg = "unknown"):
    assert_equal(format_time(actual),format_time(expected), msg)

def assert_time_correct(checkpointDist, brevetDist, startTimeStr, correctTimeStr, timeFunc, msg = "unknown"):
    start_time = arrow.get(startTimeStr,"YYYY-MM-DDTHH:mm")

    correct_time = arrow.get(correctTimeStr,"YYYY-MM-DDTHH:mm")

    returned_time = timeFunc(checkpointDist, brevetDist, start_time)

    assert_time_equal(returned_time, correct_time, msg)

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

{% for test_set in test_sets %}

##############
#
#{{test_set.name}}{% for desc_line in test_set.desc %}
# {{desc_line}}{% endfor %}
#
##############

{% for item in test_set.tests %}
#{{item.comment}}
{# the check dist has . replaced with _, because checkpoint dist can be a decimal and . can't be in python func names #}
def test_{{item.id_num}}_brevet_{{item.brev_dist}}_{{item.check_dist | string | replace(".","_")}}_{{item.timeType}}():
    brevetDist = {{item.brev_dist}}
    startDate = "{{item.start_date}}"
    dist = {{item.check_dist}}
    {{item.timeType}}Time = "{{item.time}}"

    return assert_time_correct(dist, brevetDist, startDate, {{item.timeType}}Time, {{item.timeType}}_time, "{{item.timeType}} time of checkpoint: "+str(dist)+"km")

{% endfor %}
{% endfor %}
