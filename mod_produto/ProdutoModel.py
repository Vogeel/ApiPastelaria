import db
from sqlalchemy import Column, INT, SMALLINT, VARCHAR, CHAR, BLOB, DECIMAL, String, Float, Integer


# ORM


class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True,
                        autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(200), nullable=False)
    foto = Column(BLOB, nullable=False)
    valor_unitario = Column(DECIMAL(11, 2), nullable=False)  # decimal(11,2)

    def __init__(self, id_produto, nome, descricao, foto, valor_unitario):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario

    '''
    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'
    def __str__(self):
        return self.nombre
    '''


'''
CREATE TABLE IF NOT EXISTS `tb_produto` (
  `id_produto` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `descricao` VARCHAR(200) NOT NULL,
  `foto` BLOB NULL DEFAULT NULL,
  `valor_unitario` DECIMAL(11,2) NULL DEFAULT NULL,
  PRIMARY KEY (`id_produto`))
ENGINE = InnoDB
AUTO_INCREMENT = 102
DEFAULT CHARACTER SET = latin1;
'''
