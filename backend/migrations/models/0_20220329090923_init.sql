-- upgrade --
CREATE TABLE IF NOT EXISTS "manufacturer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "website" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "car" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "website" TEXT NOT NULL,
    "image" TEXT,
    "make" TEXT NOT NULL,
    "model" TEXT NOT NULL,
    "year" INT NOT NULL,
    "cargo" DOUBLE PRECISION NOT NULL,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "manufacturer_id" INT NOT NULL REFERENCES "manufacturer" ("id") ON DELETE CASCADE,
    "user_id" INT REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "trims" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "trim" TEXT NOT NULL,
    "kwh" INT NOT NULL,
    "range" INT NOT NULL,
    "fwd" BOOL NOT NULL,
    "rwd" BOOL NOT NULL,
    "awd" BOOL NOT NULL,
    "acceleration" DOUBLE PRECISION NOT NULL,
    "horsepower" INT NOT NULL,
    "torque" INT NOT NULL,
    "mpge" DOUBLE PRECISION,
    "kwh100mi" INT,
    "charge120v" TEXT,
    "charge240v" TEXT,
    "chargeport" TEXT,
    "price" INT NOT NULL,
    "rating" DOUBLE PRECISION,
    "car_id" INT NOT NULL REFERENCES "car" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
