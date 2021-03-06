CREATE TABLE IF NOT EXISTS NSFW (
	CHANNEL_ID	INTEGER PRIMARY KEY NOT NULL,
	PERMITTED	TEXT
);

CREATE TABLE IF NOT EXISTS KARAOKE (
	SINGER_ID	INTEGER PRIMARY KEY NOT NULL
);

CREATE TABLE IF NOT EXISTS POINT_SYSTEM (
	USER_ID		INTEGER PRIMARY KEY NOT NULL,
	POINTS		INTEGER,
	LVL		    INTEGER,
	LV_CHECK	INTEGER
);

CREATE TABLE IF NOT EXISTS WANIKANI (
	USER_ID		INTEGER PRIMARY KEY NOT NULL,
	WK_KEY		TEXT,
	WK_USERNAME	TEXT
);

CREATE TABLE IF NOT EXISTS KARAOKE_LIST (
	USER_ID		INTEGER PRIMARY KEY NOT NULL,
	USER_NAME	TEXT
);

CREATE TABLE IF NOT EXISTS GITHUB_LINKS (
	ID			INTEGER PRIMARY KEY NOT NULL,
	ADDED_BY	INTEGER NOT NULL,
	ADDED_DATE	INTEGER NOT NULL,
	GH_USER		TEXT NOT NULL,
	GH_REPO		TEXT NOT NULL,
    CHANNELS    TEXT
);

CREATE TABLE IF NOT EXISTS GREET (
	SERVER_ID           INTEGER PRIMARY KEY NOT NULL UNIQUE,
	GREET_CHANNEL_ID    INTEGER NOT NULL,
	ACTIVE              TEXT NOT NULL,
    GREET_MSG           TEXT NOT NULL,
    DIRECT              TEXT
);

CREATE TABLE IF NOT EXISTS BYE (
	SERVER_ID           INTEGER PRIMARY KEY NOT NULL UNIQUE,
	BYE_CHANNEL_ID      INTEGER NOT NULL,
	ACTIVE              TEXT NOT NULL,
    BYE_MSG             TEXT NOT NULL,
    DIRECT              TEXT
);

CREATE TABLE IF NOT EXISTS AUTO_ROLE (
	SERVER_ID           INTEGER PRIMARY KEY NOT NULL UNIQUE,
    ROLE_NAME             TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS SELF_ROLE (
	SERVER_ID           INTEGER PRIMARY KEY NOT NULL,
    ROLE_NAME             TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS INVITE_FILTER (
	SERVER_ID           INTEGER PRIMARY KEY NOT NULL,
    STATUS              TEXT NOT NULL
);
