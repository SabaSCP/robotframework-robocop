*** Settings ***
Documentation  doc


*** Test Cases ***
Test
    [Tags]  sometag
    Pass
    Keyword
    One More

Golden test
    [Documentation]  This is doc
    Pass

Templated test
    [Template]  Templated keyword
    Pass


*** Keywords ***
Keyword
    [Documentation]  this is doc
    No Operation
    Pass
    No Operation
    Fail
