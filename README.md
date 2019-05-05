# HarnessPanel

*Testing a Premiere Pro Panel using nodejs*

This project is an attempt to make a very simple and easy to understand implimentation
of a NodeJS enabled Panel inside Premeire.

After reviewing several resources, and working through the samples, I found that most examples
were a bit overwhelming to get started on. To understand how to get a bare-bones panel and a simple 
nodeJS application I needed to go back, and break-down step-by-step the process to build this from scratch.

### Getting started

1) Picking a name for the project
    * I went with com.dnv.HarnessPanel
2) Create your base fileset

---

    -> .debug
        Read up on the debug section to learn more about this file.
    -> .gitignore
        Read up on the gitignore section to learn more about this file.
    -> ext.js
        Generic include from PProPanel sample.
    -> index.html
        The main interface for the sample panel.
    -> index.js
        The code behind the panel. In simple Code-View standard. 
        Will call into and return values from your ExtendScript code.
    -> index.jsx
        The ExtendScript level code behind the panel. This is where your custom Premiere code needs to go.
    -> package.json
        The NodeJS library list you need, and it *should* have your node config data.
    -> README.md
        This document.
    -> CSXS
    ---> manifest.xml
        The manifest file that will define your panel.
    -> jsx
        The contents of this folder come from the PPRO sample panel.
    ---> general.jsx
    ---> PPRO
    -----> PPro_API_Constants.jsx
    -----> Premiere.jsx
    -> lib
        The contents of this folder come from the PPRO sample panel.
    ---> CEPEngine_extensions.js
    ---> CSInterface.js
    ---> jquery-1.9.1.js
        This may need to be updated over time because it can cause security issues.
    ---> Vulcan.js

---

 3) Assign your project name and settings
    
* This is the process of populating your CSXS Manifest file. Here you need to specify the name and ID of your project (I assumed the bundle ID defaulting to the name of my main panel was enough)
---
    <ExtensionManifest Version="5.0" ExtensionBundleId="com.dnv.HarnessPanel" ExtensionBundleVersion="11.1"
    ExtensionBundleName="Remote Execution Panel" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    ...
    <ExtensionList>
        <Extension Id="com.dnv.HarnessPanel" />
	</ExtensionList>
    ...
    <DispatchInfoList>
        <Extension Id="com.dnv.HarnessPanel">
    ...
            <UI>
                <Type>Panel</Type>
                <Menu>Remote Execution Panel (Test Harness)</Menu>
---
* Configure your version, Since this is my second try on my first attempt, I am on 1.1.0
---
    <ExtensionList>
        <Extension Id="com.dnv.HarnessPanel" Version="1.1.0" />
	</ExtensionList>
---
* Assign the files for both your view and your ExtendScript code
---
    <Resources>
        <MainPath>./index.html</MainPath>
        <ScriptPath>./index.jsx</ScriptPath>
---

* Specify the permissions you need
---
    <CEFCommandLine>
        <Parameter>--enable-nodejs</Parameter>
        <Parameter>--mixed-context</Parameter>
        <Parameter>--allow-file-access</Parameter>
        <Parameter>--allow-file-access-from-files</Parameter>
    </CEFCommandLine>
---
* You should now have a complete manifest
---
    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    /*************************************************************************
    * ADOBE CONFIDENTIAL
    * ___________________
    *
    * Copyright 2014 Adobe
    * All Rights Reserved.
    *
    * NOTICE: Adobe permits you to use, modify, and distribute this file in
    * accordance with the terms of the Adobe license agreement accompanying
    * it. If you have received this file from a source other than Adobe,
    * then your use, modification, or distribution of it requires the prior
    * written permission of Adobe. 
    **************************************************************************/
    -->	
    <ExtensionManifest Version="5.0" ExtensionBundleId="com.dnv.HarnessPanel" ExtensionBundleVersion="11.1"
    ExtensionBundleName="Remote Execution Panel" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <ExtensionList>
            <Extension Id="com.dnv.HarnessPanel" Version="1.1.0" />
        </ExtensionList>
        <ExecutionEnvironment>
            <HostList>
                <Host Name="PPRO" Version="9.0" />
            </HostList>
            <LocaleList>
                <Locale Code="All" />
            </LocaleList>
            <RequiredRuntimeList>
                <RequiredRuntime Name="CSXS" Version="6.0" />
            </RequiredRuntimeList>
        </ExecutionEnvironment>

        <DispatchInfoList>
            <Extension Id="com.dnv.HarnessPanel">
                <DispatchInfo >
                    <Resources>
                        <MainPath>./index.html</MainPath>
                        <ScriptPath>./index.jsx</ScriptPath>
                        <CEFCommandLine>
                            <Parameter>--enable-nodejs</Parameter>
                            <Parameter>--mixed-context</Parameter>
                            <Parameter>--allow-file-access</Parameter>
                            <Parameter>--allow-file-access-from-files</Parameter>
                        </CEFCommandLine>
                    </Resources>
                    <Lifecycle>
                        <AutoVisible>true</AutoVisible>
                    </Lifecycle>
                    <UI>
                        <Type>Panel</Type>
                        <Menu>Remote Execution Panel (Test Harness)</Menu>
                        <Geometry>
                            <Size>
                                <Height>300</Height>
                                <Width>180</Width>
                            </Size>
                        </Geometry>
                    </UI>
                </DispatchInfo>
            </Extension>
        </DispatchInfoList>
    </ExtensionManifest>
---
4) Write your plugin
* Do what you need to do to get your plugin started. Design your HTML, include your stylings, configure your events and calls
5) Debug your code
* This was definitely the most confusing part of building a plugin; how do you debug what you wrote?
* Below is a section completely outlining how to debug your panel using VS Code, Chrome, and a text editor.
* The link that helped me understand debugging:
    * [CEP remote debugging info](https://github.com/Adobe-CEP/CEP-Resources/blob/master/CEP_8.x/Documentation/CEP%208.0%20HTML%20Extension%20Cookbook.md#Remote-Debugging)

### Debugging
There are three important details I needed to understand before I could successfully debug my panel.

1) Like all XML files, the manifest is incredibly sensitive to malformed text.
    * Make sure that you have the correct Encoding configured for the file content
    * Make sure you have the xml header block, probably the easiest to over-look error
2) Check your log files first.
    * If there is an error in initial loading, you are dead in the water, and no other debugging tool will help you.
    * Windows:

            %temp%
    * Mac:

            /Users/<USERNAME>/Library/Logs/CSXS
    * Crank your debug info to 6. There is no reason to go light when you start, get all the messages.
    * Example of a successful initalization:

            DevTools listening on 127.0.0.1:4040
    * Example of a failed initialization:

            2019-05-05 12:28:11:729 : ERROR Error occurs while getting debug port. <unspecified file>(4): expected >
    * Example of a general load error:
            [0505/123147.614:INFO:CONSOLE(36)] "Uncaught ReferenceError: run is not defined", source: file:///C:/Program%20Files%20(x86)/Common%20Files/Adobe/CEP/extensions/HarnessPanel/index.html (36)
    * There is no way to really demonstrate a success, as that just means no errors in the log.
3) Vist the Chrom debug link
    * With some work, you can configure VS Code to handle this, but I am not there yet
    * You will see the html file you specified, if you click it, you will enter Chrome's debug session

4) Remember to install your node modules
    * If you are building a panel that  uses node modules, be sure to install them in your project before you start.