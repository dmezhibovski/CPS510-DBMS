#!/bin/sh
#export LD_LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib
sqlplus64 "dmezhibo/password@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))"<<EOF

DROP TABLE C_ORDER;
DROP TABLE CUSTOMER;
DROP TABLE DRIVER;
DROP TABLE FOOD;
DROP TABLE PRODUCT;
DROP TABLE MENU;
DROP TABLE CATALOG;
DROP TABLE RESTAURANT_BRANCH;
DROP TABLE STORE_BRANCH;
DROP TABLE RESTAURANT;
DROP TABLE GROCERY_STORE;
exit;

EOF