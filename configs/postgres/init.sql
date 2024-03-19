create table usuarios (
    id serial primary key,
    nome varchar(255),
    dt_nascimento date
);
insert into usuarios (id, nome, dt_nascimento) VALUES (1, 'Joao', '1993-02-01');
insert into usuarios (id, nome, dt_nascimento) VALUES (2, 'Jefferson', '1990-09-01');
insert into usuarios (id, nome, dt_nascimento) VALUES (3, 'Janderson Neto', '1995-05-01');
insert into usuarios (id, nome, dt_nascimento) VALUES (4, 'Hamilton Lima', '1995-02-20');
insert into usuarios (id, nome, dt_nascimento) VALUES (5, '{"erro": "not found 404"}', '1995-01-20');
