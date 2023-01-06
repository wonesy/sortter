create table if not exists support_requests (
    id serial primary key,
    first_name text not null,
    last_name text not null,
    email text not null,
    phone text not null,
    description text not null,
    unique (first_name, last_name, email, phone, description)
);