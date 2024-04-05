TO create a log file while recompiling COBOL in UNIX/LINUX

\------------------------------------------------------------------------

cobol\_name  | tee -i path/filename.log

Example:

./pscbl.mak | tee -i /u01/app/psoft/pshomes/csdev/setup/cobol\_csdev1.log

\-------------------------------------------------------------------------


openssl s\_client -connect pay.nottingham.edu.cn:443  | tee -i /u01/app/psoft/webserver\_csprd.log

example:

sh pskeymanager.sh -list  | tee -i /u01/app/psoft/curl1\_csprd.log



