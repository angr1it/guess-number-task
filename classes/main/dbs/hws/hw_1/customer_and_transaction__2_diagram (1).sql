CREATE TABLE "transaction" (
  "id" serial PRIMARY KEY,
  "transaction_date" date,
  "online_order" bool,
  "order_status" varchar(16),
  "product_id" serial,
  "customer_id" serial
);

CREATE TABLE "product" (
  "id" serial PRIMARY KEY,
  "product_id_old" int,
  "brand" varchar(32),
  "product_line" varchar(16),
  "product_class" varchar(16),
  "product_size" varchar(16),
  "list_price" numeric,
  "standard_cost" numeric
);

CREATE TABLE "customer" (
  "id" serial PRIMARY KEY,
  "first_name" varchar(32),
  "last_name" varchar(32),
  "gender" varchar(6),
  "dob" date,
  "job_title" varchar(64),
  "job_industry_category" varchar(64),
  "wealth_segment" varchar(32),
  "deceased_indicator" char(1),
  "owns_car" bool
);

CREATE TABLE "address" (
  "id" serial PRIMARY KEY,
  "address" text,
  "postcode" smallint,
  "state" varchar(32),
  "country" varchar(32),
  "property_valuation" int,
  "customer_id" int
);

ALTER TABLE "transaction" ADD FOREIGN KEY ("product_id") REFERENCES "product" ("id");

ALTER TABLE "transaction" ADD FOREIGN KEY ("customer_id") REFERENCES "customer" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("customer_id") REFERENCES "customer" ("id");
