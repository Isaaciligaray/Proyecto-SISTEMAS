create database BDMonoV8;

use BDMonoV8;

create table Clientes(
	id_cliente int auto_increment primary key,
    Nombre varchar(250) not null,
    total_compra int(7)
    );

create table Facturas(
	id_factura int auto_increment primary key,
    id_cliente int,
    monto_total int(9),
    fecha date,
    foreign key (id_cliente) references Clientes(id_cliente) 
    );

create table MIA_vendidos(
	MIA varchar(15) primary key,
    id_factura int,
    CIF decimal(6,2) not null,
    peso decimal(6,2) not null,
    total_aduana int(7) not null,
    foreign key (id_factura) references Facturas(id_factura)
    );

Insert into Clientes values ("1" ,"Segutec", "399000");

Insert into Facturas values ("89", "1", "339000","2024-03-29");

Insert into MIA_vendidos values ("MIA000040852453", "89", "127.79","4.46","33839");
Insert into MIA_vendidos values ("MIA000040852501", "89", "146.77","7.24","50219");

select*from mia_vendidos;

SELECT YEAR(fecha) AS Año, MONTH(fecha) AS Mes, sum(monto_total) AS "Total facturado"
FROM Facturas
GROUP BY YEAR(fecha), MONTH(fecha)
ORDER BY Año, Mes;

SELECT id_cliente, Nombre, SUM(total_compra) AS Suma_Compras
FROM Clientes
GROUP BY id_cliente, Nombre
ORDER BY Suma_Compras DESC;