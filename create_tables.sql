-- public."user" definition

-- Drop table

-- DROP TABLE public."user";

CREATE TABLE public."user" (
	id serial4 NOT NULL,
	username varchar(20) NOT NULL,
	"password" varchar(100) NOT NULL,
	correo varchar(100) NOT NULL,
	direccion varchar(150) NULL,
	telefono varchar(9) NULL,
	"createdAt" timestamp NOT NULL,
	CONSTRAINT user_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX user_correo ON public."user" USING btree (correo);
CREATE UNIQUE INDEX user_username ON public."user" USING btree (username);