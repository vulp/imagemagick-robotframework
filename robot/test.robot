*** Settings ***
Documentation   jotain
Test Teardown   Close All And Update
Resource        resources.robot

Force Tags      demo

*** Test Cases ***
testi
	Make Image Difference