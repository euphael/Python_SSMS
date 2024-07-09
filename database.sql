CREATE DATABASE MarketPlace;
GO

USE MarketPlace;
GO

CREATE TABLE Cliente (
    IdCliente INT PRIMARY KEY,
    Nome NVARCHAR(100),
    Email NVARCHAR(100)
);
GO

-- Inserir dados de exemplo na tabela "Cliente"
INSERT INTO Cliente (IdCliente, Nome, Email)
VALUES 
    (1, 'João Silva', 'joao.silva@example.com'),
    (2, 'Maria Santos', 'maria.santos@example.com');
GO

select * from Cliente