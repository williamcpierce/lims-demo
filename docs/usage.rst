Usage
=====

Access
------------

This demo is hosted live on my website, where you can use these credentials to log in to a 
demo account:

| URL: `williampierce.io/lims <https://williampierce.io/lims>`_
| Username: demo
| Password: demo


Features
------------

Sample Registry
^^^^^^^^^^^^
This view is where samples are registered, and allows for searching and filtering of the 
samples (by type) while browsing. Click on a sample ID to see all the available fields for 
that sample, as only a subset is shown in the main table. 

To register a new sample, click the green + icon on the top right, select a sample type, and 
then click "Save and Continue Editing" to load the additional fields from the type definition. 
Samples IDs are automatically assigned by combining the type prefix with the primary key of 
that sample in the sample database table, to ensure uniqueness. 

Samples may also be registered in bulk using the import tool. To do so, construct a file 
(such as .csv or .xlsx) in the following format:

.. list-table::
   :widths: 20 30 20 30 
   :header-rows: 1

   * - type
     - alias
     - related
     - sequence
   * - OLI
     - Cas9 Guide 29
     - PRO003
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

Sample Type Definitions
^^^^^^^^^^^^
Users of this app can define their own sample types. These definitions consist of a type 
prefix, which is prepended to the ID of each sample of that type (e.g. PRO for protein), and 
a selection of form fields to show on the registration form for that sample type. 

Field customization allows for users to specify which data can be associated with each sample 
type - for example, one might include the "Sequence" field for oligonucleotides but omit it 
for chemical reagents. 

Container Registry
^^^^^^^^^^^^
Functioning similar to the sample registry, this view shows all registered containers, and is 
where new containers are registered. 

Containers can be registered either via the registration form, or bulk uploaded with the 
import tool, with an input file in the following format:

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
The location registry uses a hierarchical structure to define locations where containers can 
reside. Each location has an optional parent, and multiple locations can have the same parent 
location. 

This hierarchical data is represented in the database using modified preorder tree transversal, 
a technique which optimizes retrieval of the tree structure (the main operation needed for 
this use case) at the expense of efficiency when inserting or modifying the tree (comparatively 
rare). 

Audit Trail
^^^^^^^^^^^^
All operations performed on any of the other tables are recorded as log entries in an audit 
trail table. This helps ensure data integrity, and can also assist with reverting unintended 
changes.  

Users and Groups
^^^^^^^^^^^^
Django provides models for users and user groups out of the box. These enable attribution of 
actions taken in the LIMS (such as in the audit log), and limiting of permissions for a 
given group of users. This could be used to restrict the ability of lab users to delete 
sample types or locations, restricting those actions to administrators and power users. 

API
^^^^^^^^^^^^
GET endpoints are provided for the Sample, Type, Container, and Location tables. These 
routes are built using Django REST Framework, a module for building RESTful APIs in 
Django. They can be accessed via URLs in the following formats:

| williampierce.io/api/<table>/
| williampierce.io/api/<table>/<pk>/

For example:

| List all samples: `williampierce.io/api/sample/ <https://williampierce.io/api/sample/>`_
| Detail on one sample: `williampierce.io/api/sample/2/ <https://williampierce.io/api/sample/2/>`_
| JSON format: `williampierce.io/api/sample/?format=json <https://williampierce.io/api/sample/?format=json>`_

