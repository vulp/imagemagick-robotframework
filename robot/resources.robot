*** Settings ***
Library           Selenium2Library
Library           Custom.py

Resource         variables.robot

*** Keywords ***
Close All And Update
	Close Browser
    update data         ${TEST NAME}    ${SUITE NAME}       ${TEST STATUS}

Set Image Dir
    [Documentation]     set screenshots or baseimages directory

    Run Keyword If      '${BASEIMAGE}' == 'False'       Set Screenshot Directory	    ${CURDIR}${/}screenshots
    ...     ELSE        Set Screenshot Directory	    ${CURDIR}${/}baseimages

Take Screenshot To Image Dir
    [Documentation]     takes screenshot to baseimages folder or screenshots folder based on BASEIMAGE variable

	Open Browser		http://localhost		chrome
	Run Keyword If      '${BASEIMAGE}' == 'False'        Capture Page Screenshot     	screenshot.png
	...                 ELSE                            Capture Page Screenshot     	${TEST NAME}.png

    #Run Keyword If      '${BASEIMAGE}' == 'True'        save data                      ${TEST NAME}    ${SUITE NAME}

Make Image Difference
    [Documentation]         Set Image Dir
    ...                     Take Screenshot To Image Dir
    ...                     image difference    ${TEST NAME}    ${SUITE NAME}

    Set Image Dir
    Take Screenshot To Image Dir

    ${accepted} =           image difference    ${TEST NAME}    ${SUITE NAME}
    Run Keyword If          '${accepted}' == 'True'             Pass Execution          ${TEST NAME} ok
    ...       ELSE          Create Result           ${accepted}


Create Result
    [Arguments]             ${value}
    Log                     <b>new vs difference</b><div><img src="${CURDIR}${/}screenshots${/}screenshot.png" style="width: 50%;"><img src="${CURDIR}${/}baseimages${/}${TEST NAME}_diff.png" style="width: 50%;"></div><b>baseimage</b><img src="${CURDIR}${/}baseimages${/}${TEST NAME}.png" style="width: 50%;">                 html=yes
    Log                     <b>baseimage</b><img src="${CURDIR}${/}baseimages${/}${TEST NAME}.png" style="width: 50%;">                 html=yes
    Fail                                                        ${TEST NAME} different pixels: ${value}
