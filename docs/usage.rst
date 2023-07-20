Usage
=====

Access
------------

To test this demo, you can access it here:

| URL: `williampierce.io <https://williampierce.io/>`_
| Username: demo
| Password: demo


Features
------------

Sample Type Definitions
^^^^^^^^^^^^
Users can define their own sample types. These definitions consist of a 
type prefix, which is prepended to each sample of that type (e.g. PRO for 
protein), and a selection of form fields to show on the registration form 
for that sample type. 

Sample Registry
^^^^^^^^^^^^
This view is where samples are registered, and allows for searching and 
filtering of the samples (by type) while browsing. Click on a sample ID 
to see all the available fields for that sample, as only a subset are 
shown in the main table. 

To register a new sample, click the green + icon in the top right, 
select a sample type, and then click "Save and Continue Editing" to 
load the additional fields from the type definition. Samples IDs are 
automatically assigned by combining the type prefix with the primary 
key of that sample in the sample database table. 

Samples may also be registered in bulk using the import tool. To do so, 
construct a file (such as .csv or .xlsx) in the following format:

.. list-table::
   :widths: 20 30 20 30 
   :header-rows: 1

   * - type
     - alias
     - related
     - sequence
   * - OLI
     - Cas9 Guide 29
     - PRO002
     - ATCTTGTGGAAA[...]
   * - PRO
     - Cas12a
     - 
     -  

| Where:
| "type" is the prefix for the desired sample type (required)
| "alias" is an alternate name for the sample (optional)
| "related" is the ID of another related sample (optional)
| "sequence" is a DNA/RNA/AA sequence for the sample (optional)

Container Registry
^^^^^^^^^^^^
Functioning similar to the sample registry, this view shows all 
registered containers, and is where new containers are registered. 

Containers can be registered either via the registration form, or 
bulk uploaded with the import tool, with an input file in the 
following format:

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - barcode
     - location
     - contents
   * - XY52083
     - Box 1
     - OLI004,OLI011
   * - XY52084
     - Box 1
     - PRO002

| Where:
| "barcode" is the unique identifier for the container (required)
| "location" is the name of a location from the location registry (optional)
| "contents" is a comma-separated list of sample IDs (optional)

Location Registry
^^^^^^^^^^^^
The location registry uses a hierarchical structure to define 
locations where containers can reside. Each location has an optional 
parent, and multiple locations can have the same parent location. 

This hierarchical data is represented in the database using modified 
preorder tree transversal, a technique which optimizes retrieval of 
the tree structure (the main operation needed for this use case) at 
the expense of efficiency when inserting or modifying the tree 
(comparatively rare). 

Audit Trail
^^^^^^^^^^^^
All operations performed on any of the other tables are recorded 
as log entries in an audit trail table. This helps ensure 
data integrity, and can also assist in identifying unintended changes 
so they can be reverted. 
