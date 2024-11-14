*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  newuser
    Set Password  validpass123
    Confirm Password  validpass123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  us
    Set Password  validpass123
    Confirm Password  validpass123
    Submit Registration
    Registration Should Fail With Message  Username too short

Register With Invalid Username And Valid Password
    Set Username   Us84
    Set Password   validpass123
    Confirm Password    validpass123
    Submit Registration
    Registration Should Fail With Message   Username must contain only lower case letters

Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  short
    Confirm Password  short
    Submit Registration
    Registration Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  validuser
    Set Password  password
    Confirm Password  password
    Submit Registration
    Registration Should Fail With Message  Password can't contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  validpass123
    Confirm Password  differentpass123
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Reset Application Create User And Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Submit Registration
    Registration Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  username
    Set Password  password1
    Confirm Password  password1
    Submit Registration
    Registration Should Succeed
    Go To Main Page
    Press Logout
    Set Username  username
    Set Password  password1
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  user
    Set Password  password
    Confirm Password  password
    Submit Registration
    Go To Login Page
    Set Username  user
    Set Password  password
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Press Logout
    Click Button  Logout

Press
    Click Button  Main

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page