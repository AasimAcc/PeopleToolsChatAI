PeopleTools Upgrade Process Breakdown
This document outlines the steps involved in a PeopleTools upgrade process. Here's a breakdown of each step:

Preparation (a, b, c):

a) Build a new environment D1: This environment will be used for comparison and retrofitting purposes with the latest tools version (8.60).
b) Build new Dev and UAT environments: These environments (Dev and UAT) will be created by copying the existing production environments (T58 and Q58) and upgraded to the previous tools version (8.59). They will serve as the development and testing paths during the upgrade.
c) Create a new Stat flow: A new workflow (Stat flow) will be built to handle data migration from Dev and UAT to the production environment.
Upgrade and Testing in D1 (d, e, f):

d) Synchronize Dev and UAT environments: These environments (Dev and UAT) will be kept in sync with their corresponding production counterparts (T58 and Q58) throughout the upgrade process.
e) Object Comparison and Retrofitting: The objects in the upgraded environment (D1) will be compared to the objects in the existing production environment (likely T58). Any changes required for compatibility with the new tools version (8.60) will be identified and implemented as retrofits.
f) Test Functionality of Retrofitted Objects: Once the retrofits are applied, the functionality of the affected objects in D1 will be thoroughly tested to ensure they work as expected.
Production Upgrade and Migration (g, h, i):

g) Upgrade T58 Environment (Manual): The T58 environment (original production) will be upgraded to the new tools version (8.60) by the Admin team.
h) Migrate Retrofitted Objects to T58: The retrofitted objects from D1 will be migrated to the upgraded T58 environment using database migration techniques.
i) System Testing in T58: After migration, system testing will be performed on the affected objects in T58 to verify that all changes have been migrated correctly.
UAT and Production Cutover (j, k, l):

j) Prepare for Q58 Upgrade: Once system testing in T58 is complete, a Change Request System (CSR) will be prepared to migrate the changes to the UAT environment (Q58).
k) Upgrade Q58 Environment and Migrate Changes: Before upgrading Q58, all automated jobs (Autosys jobs) in this environment will be put on hold. The Tech Arch team will then upgrade Q58 and migrate the changes from T58.
l) UAT Testing and Production Checkout: Developers will verify that all changes have been migrated correctly in Q58. Business users will then perform User Acceptance Testing (UAT) on all functionalities. After successful UAT, a final CSR will be prepared to migrate the changes to the production environment (P58).
m) Production Upgrade and Post-Upgrade Checks: Similar to Q58, Autosys jobs in P58 will be placed on hold before the upgrade. The Tech Arch team will then upgrade P58 and migrate the retrofits from Q58. Developers will again check for successful migration, and business users will perform a final production checkout. Finally, Autosys jobs will be resumed.
Data Verification (m, n):

m) Row Count Analysis: The number of rows (data) in critical tables will be compared before and after the upgrade across all environments (D1, T58, Q58, and P58) to ensure no data loss or corruption has occurred.
n) Audit Analysis: System audit logs (SYSAUDIT, DDDAUDIT, SWAPAUDIT) will be analyzed across all environments to identify and correct any discrepancies. It's important to avoid modifying delivered objects unless there are specific customizations required.
