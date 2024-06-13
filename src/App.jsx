import './App.css';
import carrito from './assets/carrito.png';

function App() {

    return (
        <main className='app'>
            <h4 className='success'>You are done</h4>
            <div className="header">
                <h1>Shopping List</h1>
                <img src={carrito} alt="some img" />
                <input type="text" placeholder="Add an item" />
            </div>
            <ul>
                <li>
                    <div className="container">
                        <input type="checkbox" name="" id="" />
                        <p>Carrots</p>
                    </div>
                </li>
            </ul>
        </main>
    )
}

export default App
