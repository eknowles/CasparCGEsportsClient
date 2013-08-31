import PyQt4

QSqlDatabase db = QSqlDatabase.addDatabase("QMYSQL");
db.setHostName("eknowles.com");
db.setDatabaseName("admin_escg");
db.setUserName("admin_escg");
db.setPassword("p4e9@;FImZ8[");
bool ok = db.open();

QSqlQuery query;
query.exec("SELECT id, name, location, start_date FROM events");