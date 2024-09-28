CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE payments (id INTEGER PRIMARY KEY AUTOINCREMENT, tgid INTEGER UNIQUE ON CONFLICT IGNORE, bill_id TEXT, amount INTEGER, time_to_add BIGINT, mesid TEXT);
CREATE TABLE userss (id INTEGER PRIMARY KEY AUTOINCREMENT, tgid INTEGER UNIQUE ON CONFLICT IGNORE, subscription TEXT DEFAULT none, banned BOOLEAN DEFAULT (false), notion_oneday BOOLEAN DEFAULT (false), username STRING DEFAULT none, fullname STRING DEFAULT none, wg_key TEXT, trial_continue integer, referrer_id INTEGER);
CREATE TABLE static_profiles (id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING);
