*** Settings ***
Library  SeleniumLibrary
Library  RequestsLibrary

*** Variables ***
${UI_URL}  https://practice.expandtesting.com/notes/app
${API_URL}  https://practice.expandtesting.com/notes/api

*** Test Cases ***
Login by UI and add a note
    Open Browser  ${UI_URL}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/notes/app/login"]
    Input Text  id=email  nira18me@cmrit.ac.in
    Input Text    id=password    qwerty
    Click Button  xpath=//button[@data-testid="login-submit"]
    Sleep    2s
    Click Element    xpath=//button[text()="+ Add Note"]
    Sleep    2s
    Input Text    xpath=//input[@id="title"]    movies
    Input Text    xpath=//textarea[@id="description"]    List of Horror movies

    Click Button  xpath=//button[@data-testid="note-submit"]
    Sleep    2s
    Page Should Contain    movies
    Page Should Contain    List of Horror movies

    Set Suite Variable    ${UI_TITLE}          movies
    Set Suite Variable    ${UI_DESCRIPTION}    List of Horror movies

    Close All Browsers

Authentication by API and get note
    Create Session  notes_api  ${API_URL}  verify=True
    ${form_data}  Create Dictionary  email=nira18me@cmrit.ac.in  password=qwerty
    ${response1}=  POST On Session  notes_api  /users/login  data=${form_data}

    Should Be Equal As Strings  ${response1.status_code}  200

    ${body}  Set Variable  ${response1.json()}

    Log To Console    ${body}

    ${token}  Set Variable  ${body['data']['token']}
    Log To Console    ${token}

    ${headers}  Create Dictionary  x-auth-token=${token}

    ${response2}=  Get On Session  notes_api  /notes  headers=${headers}

    Should Be Equal As Strings  ${response2.status_code}  200

    ${notes}  Set Variable  ${response2.json()['data']}
    Log To Console    ${notes}

    FOR    ${note}    IN    @{notes}
        IF    '${note['title']}' == '${UI_TITLE}'
            Set Suite Variable    ${API_TITLE}          ${note['title']}
            Set Suite Variable    ${API_DESCRIPTION}    ${note['description']}
            Log To Console    API Title: ${note['title']}
            Log To Console    API Desc : ${note['description']}

        END
    END

Cross validation of UI and API
    Should Be Equal    ${UI_TITLE}    ${API_TITLE}
    Log To Console    matched
    Should Be Equal    ${UI_DESCRIPTION}    ${API_DESCRIPTION}
    Log To Console    matched



