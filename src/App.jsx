import './App.css';
import React from 'react';
import { Item } from './Item';
import carrito from './assets/carrito.png';
import { useState } from 'react';

function App() {

    const [inputValue, setInputValue] = useState("");
    const [items, setItems] = useState([]);

    function handleChangeInputValue(event) {
        setInputValue(event.target.value);
    }

    function handleKeyDown(event) {
        if (event.key === "Enter") {
            setItems([...items, { value: inputValue }]);
            setInputValue("");
        }
    }

    function handleRemoveItem(index) {
        setItems(items.filter((item, i) => i !== index));
    }

    return (
        <main className='app'>
            <h4 className='success'>You are done</h4>
            <div className="header">
                <h1>Shopping List</h1>
                <img src={carrito} alt="some img" />
                <input
                    type="text"
                    placeholder="Add an item"
                    className="item-input"
                    value={inputValue}
                    onChange={handleChangeInputValue}
                    onKeyDown={handleKeyDown}
                />
            </div>
            <ul>
                {items.map((item, index) => (
                    <Item
                        key={index}
                        value={item.value}
                        handleRemoveItem={() => handleRemoveItem(index)}
                    />
                ))}
            </ul>
        </main>
    )
}

export default App
