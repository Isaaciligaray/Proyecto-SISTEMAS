create database BDMonoV8;

use BDMonoV8;

create table Clientes(
	id_cliente int auto_increment primary key,
    Nombre varchar(250) not null
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

Insert into Clientes values ("1" ,"Segutec");

Insert into Facturas values ("89", "1", "339000","2024-03-29");

Insert into MIA_vendidos values ("MIA000040852453", "89", "127.79","4.46","33839");
Insert into MIA_vendidos values ("MIA000040852501", "89", "146.77","7.24","50219");

select*from mia_vendidos order by id_factura asc;

SELECT YEAR(fecha) AS Año, MONTH(fecha) AS Mes, sum(monto_total) AS "Total facturado"
FROM Facturas
GROUP BY YEAR(fecha), MONTH(fecha)
ORDER BY Año, Mes;

SELECT DATE_FORMAT(fecha, '%Y-%m') AS 'Año-Mes', SUM(monto_total) AS 'Total facturado'
FROM Facturas
GROUP BY DATE_FORMAT(fecha, '%Y-%m')
ORDER BY 'Año-Mes';

select Nombre, Facturas.monto_total from Clientes where id_cliente = Facturas.id_cliente group by Nombre;

SELECT c.Nombre, SUM(f.monto_total) AS Total_Compras
FROM Clientes c
JOIN Facturas f ON c.id_cliente = f.id_cliente
GROUP BY c.Nombre
ORDER BY Total_Compras DESC;

SELECT c.Nombre, SUM(f.monto_total) AS Total_Compras
FROM Clientes c
JOIN Facturas f ON c.id_cliente = f.id_cliente
GROUP BY c.Nombre
ORDER BY Total_Compras DESC
LIMIT 5;