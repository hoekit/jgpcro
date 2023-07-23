# jgpcro - Semi-automating time tracking and invoicing

## Contents
[
1. Use Case
]

## Details

----
<a id="1"></a>
## 1. Use Case
__ Timelog: Current State

Whenever I work on an issue or problem for GPCRO, I'd do the following:

    Start the Timelog spreadsheet.

    Capture the start time in the spreadsheet (using a macro).

    Work on the issue or problem.

    Capture the end time in the spreadsheet (using a macro). 

..
__ Timelog: Target State

Automate the above using a program, jgpcro:

    jgpcro activity_start
        Logs the start of an activity

    jgpcro activity_stop
        Logs the end of an activity

..
__ Invoicing: Current State

Every quarter, to invoice, there's a procedure to generate the files and
so on:

    Manually create the timesheet using a template

    Manually create the invoice using a template

    Manually create the receipt using a template

..
__ Invoicing: Target State

The goal is to automate the above:

    jgpcro timesheet_create
        Create the timesheet document for invoicing

    jgpcro invoice_create
        Create the invoice for quarterly invoicing

    jgpcro receipt_create
        Create the receipt for quarterly invoicing

..

