*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}           https://practice.expandtesting.com/notes/app
${USERNAME}      nira18me@cmrit.ac.in
${PASSWORD}      qwerty
${BROWSER}       Chrome

# Selector Variables
${USERNAME_FIELD}        id=email
${PASSWORD_FIELD}        id=password
${LOGIN_BUTTON}          xpath=//button[@type='submit' and contains(text(), 'Login')]
${SUCCESS_INDICATOR}     xpath=//*[contains(text(), 'Add Note')]

*** Test Cases ***
Login Test
    [Documentation]    Test login functionality for notes app
    [Tags]    smoke    login
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Navigate To Login Page
    Wait Until Element Is Visible    ${USERNAME_FIELD}    10s
    Input Text    ${USERNAME_FIELD}    ${USERNAME}
    Input Text    ${PASSWORD_FIELD}    ${PASSWORD}
    Click Button    ${LOGIN_BUTTON}
    Wait Until Page Contains Element    ${SUCCESS_INDICATOR}    10s
    [Teardown]    Close Browser

*** Keywords ***
Navigate To Login Page
    [Documentation]    Navigate directly to the login page
    Go To    ${URL}/login
    Wait Until Page Contains Element    id=email    10s

