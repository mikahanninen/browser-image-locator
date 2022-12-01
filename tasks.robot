*** Settings ***
Library     ExtendedSelenium.py
Library     RPA.Images


*** Variables ***
${webpage_image}                %{ROBOT_ARTIFACTS}${/}webpage.png
${documentation_link_image}     %{ROBOT_ROOT}${/}images${/}documentation_link.png


*** Tasks ***
Minimal task
    Open Available Browser
    ...    https://portal.robocorp.com
    ...    headless=${TRUE}
    ...    maximized=${TRUE}
    ${size}=    Get Window Size
    Log To Console    ${size}
    Screenshot    filename=${webpage_image}
    ${regions}=    Find Template In Image    ${webpage_image}    ${documentation_link_image}    tolerance="0.7"
    Log To Console    ${regions}
    Click Region    ${regions}[0]
    Sleep    5s
    Screenshot    filename=%{ROBOT_ARTIFACTS}${/}after_region_click.png
    Log    Done.
