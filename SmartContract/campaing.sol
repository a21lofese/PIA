/**
    Enunciado:

    Hay que desarrollar un contrato en Etherium que permita gestionar una campaña de recogida de fondos.
    Nuestra campaña tiene un saldo (inicialmente de 0 euros) y una lista con los movimientos efectuados (inicialmente cada movimiento es un string y opcionalmente un registro con diferentes campos). Además tiene las siguientes opciones:
    1. Ingreso. Recibe una cantidad (positiva y float) que incrementa el saldo y el nombre de quien ingresa (string). Además añade a la lista de movimientos uno nuevo con la descripción del movimiento: fecha (opcional, se saca del sistema), "Ingreso de ", cantidad correspondiente, "Donante:", persona que lo ingresa y el id de su cartera.
    2. Gasto. Recibe un importe. Solo el propietario del contrato puede ejecutar esta opción y es necesario que haya saldo suficiente. También cambia el saldo y genera un movimiento.
    3. Ver saldo de la campaña.
    4. Ver movimientos (solo el dueño).
 */

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Campaign {
    address owner;
    uint256 balance = 0;
    Movement[] movements;

    struct Movement {
        uint256 amount;
        string donor;
        address donorAddress;
        uint256 timestamp;
    }

    constructor() {
        owner = msg.sender;
    }

    function deposit(uint256 amount, string calldata donor) public {
        require(amount > 0, "Error, la cantidad debe ser positiva");
        balance += amount;
        movements.push(Movement(amount, donor, msg.sender, block.timestamp));
    }

    function withdraw(uint256 amount) public {
        require(msg.sender == owner, "Error, solo el propietario puede retirar fondos");
        require(balance >= amount, "Error, no hay saldo suficiente");
        balance -= amount;
        movements.push(Movement(amount, "", address(0), block.timestamp));
    }

    function getBalance() public view returns (uint256) {
        return balance;
    }

    function getMovements() public view returns (Movement[] memory) {
        require(msg.sender == owner, "Error, solo el propietario puede ver los movimientos");
        return movements;
    }
}
