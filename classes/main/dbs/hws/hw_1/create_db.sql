CREATE TABLE
    customer (
        id serial primary key,
        first_name varchar (32) not null,
        last_name varchar (32),
        gender varchar (6) not null,
        dob date,
        job_title varchar (64),
        job_industry_category varchar (64),
        wealth_segment varchar (32) not null,
        deceased_indicator char (1) not null,
        owns_car boolean not null
    );

CREATE TABLE
    product (
        id serial primary key,
        product_id_old int not null,
        brand varchar (32) not null,
        product_line varchar (16) not null,
        product_class varchar (16) not null,
        product_size varchar (16) not null,
        list_price numeric,
        standard_cost numeric
    );

CREATE TABLE
    transaction (
        id serial primary key,
        customer_id serial references customer (id),
        product_id serial references product (id),
        transaction_date date,
        online_order bool,
        order_status varchar (16)
    );

CREATE TABLE
    address (
        id serial primary key,
        address text not null,
        postcode char (4) not null,
        state varchar (32) not null,
        country varchar (32) not null,
        property_valuation int not null,
        customer_id serial references customer (id)
    );

