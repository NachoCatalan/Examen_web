-- Generado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   en:        2024-07-13 17:17:20 CLT
--   sitio:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE cliente (
    id_cliente  NUMBER(3) NOT NULL,
    run_cliente NUMBER(8) NOT NULL,
    dv_cliente  VARCHAR2(1 CHAR) NOT NULL,
    pnombre     VARCHAR2(25 CHAR) NOT NULL,
    snombre     VARCHAR2(25 CHAR),
    apaterno    VARCHAR2(25 CHAR) NOT NULL,
    amaterno    VARCHAR2(25 CHAR) NOT NULL,
    telefono    NUMBER(9) NOT NULL,
    direccion   VARCHAR2(50 CHAR) NOT NULL,
    correo      VARCHAR2(50 CHAR) NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente );

CREATE TABLE descuento (
    id_descuento NUMBER(3) NOT NULL,
    nombre_dscto VARCHAR2(20 CHAR) NOT NULL,
    porcentaje   NUMBER(3) NOT NULL
);

ALTER TABLE descuento ADD CONSTRAINT descuento_pk PRIMARY KEY ( id_descuento );

CREATE TABLE producto (
    id_producto                    NUMBER(3) NOT NULL,
    nombre_producto                VARCHAR2(30 CHAR) NOT NULL,
    precio_unidad                  NUMBER(8) NOT NULL,
    descripcion                    VARCHAR2(50 CHAR) NOT NULL,
    tipo_producto_id_tipo_producto NUMBER(3) NOT NULL
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( id_producto );

CREATE TABLE tipo_producto (
    id_tipo_producto   NUMBER(3) NOT NULL,
    desc_tipo_producto VARCHAR2(50 CHAR) NOT NULL
);

ALTER TABLE tipo_producto ADD CONSTRAINT tipo_producto_pk PRIMARY KEY ( id_tipo_producto );

CREATE TABLE venta_producto (
    id_venta_producto      NUMBER(3) NOT NULL,
    precio_total           NUMBER(10) NOT NULL,
    producto_id_producto   NUMBER(3) NOT NULL,
    cliente_id_cliente     NUMBER(3) NOT NULL,
    total_unidades         NUMBER(3) NOT NULL,
    fecha                  DATE,
    descuento_id_descuento NUMBER(3) NOT NULL
);

ALTER TABLE venta_producto ADD CONSTRAINT venta_producto_pk PRIMARY KEY ( id_venta_producto );

ALTER TABLE producto
    ADD CONSTRAINT producto_tipo_producto_fk FOREIGN KEY ( tipo_producto_id_tipo_producto )
        REFERENCES tipo_producto ( id_tipo_producto );

ALTER TABLE venta_producto
    ADD CONSTRAINT venta_producto_cliente_fk FOREIGN KEY ( cliente_id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE venta_producto
    ADD CONSTRAINT venta_producto_descuento_fk FOREIGN KEY ( descuento_id_descuento )
        REFERENCES descuento ( id_descuento );

ALTER TABLE venta_producto
    ADD CONSTRAINT venta_producto_producto_fk FOREIGN KEY ( producto_id_producto )
        REFERENCES producto ( id_producto );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             5
-- CREATE INDEX                             0
-- ALTER TABLE                              9
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
