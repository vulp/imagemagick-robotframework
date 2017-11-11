*** Settings ***
Documentation   jotain
Test Teardown   Close All
Resource        resources.robot

Force Tags      demo

*** Test Cases ***
testi
	Make Image Difference