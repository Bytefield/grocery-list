import React, { useState } from 'react';
import { Item } from './Item';
import './styles/css/App.css';

function App() {
    const [feature, setFeature] = useState('');
    const [featureTags, setFeatureTags] = useState([]);
    const [background, setBackground] = useState('');
    const [scenario, setScenario] = useState('');
    const [scenarioTags, setScenarioTags] = useState([]);
    const [step, setStep] = useState('');
    const [items, setItems] = useState([]);

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            setItems(prevItems => [...prevItems, { feature, featureTags, background, scenario, scenarioTags, step }]);
            setFeature('');
            setFeatureTags([]);
            setBackground('');
            setScenario('');
            setScenarioTags([]);
            setStep('');
            setDescription('');
        }
    };

    const handleChangeFeature = (event) => {
        setFeature(event.target.value);
    }

    const handleChangeFeatureTags = (event) => {
        setFeatureTags(event.target.value.split(','));
    }

    const handleChangeBackground = (event) => {
        setBackground(event.target.value);
    }

    const handleChangeScenario = (event) => {
        setScenario(event.target.value);
    }

    const handleChangeScenarioTags = (event) => {
        setScenarioTags(event.target.value.split(','));
    }

    const handleChangeStep = (event) => {
        setStep(event.target.value);
    }

    const handleRemoveItem = (index) => {
        setItems(prevItems => prevItems.filter((item, itemIndex) => itemIndex !== index));
    }

    const fetch_data = () => {
        fetch('http://localhost:5000/api/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: 'The data you want to tokenize' }),
        })
            .then(async response => {
                if (!response.ok) {
                    const text = await response.text();
                    throw new Error(text);
                }
                return response.json();
            })
            .then(data => console.log(data))
            .catch((error) => console.error('Error:', error));
    }

    return (
        <main className="App">
            <div className="input_bar">
                <div className="feature">
                    <input type="text" placeholder="Feature Tags" value={featureTags} onChange={handleChangeFeatureTags} />
                    <input type="text" placeholder="Feature" value={feature} onChange={handleChangeFeature} />
                </div>
                <div className="scenario">
                    <input type="text" placeholder="Scenario Tags" value={scenarioTags} onChange={handleChangeScenarioTags} />
                    <input type="text" placeholder="Scenario description" value={scenario} onChange={handleChangeScenario} />
                    <div className="step">
                        <input type="text" placeholder="Step description" value={step} onChange={handleChangeStep} onKeyDown={handleKeyDown} />
                    </div>
                </div>
            </div>
            <button onClick={fetch_data}>Fetch Data</button>
            <ul>
                {items.map((item, index) => (
                    <Item
                        key={index}
                        feature={item.feature}
                        featureTags={item.featureTags}
                        scenario={item.scenario}
                        scenarioTags={item.scenarioTags}
                        step={item.step}
                        handleRemoveItem={() => handleRemoveItem(index)}
                    />
                ))}
            </ul>
        </main>
    );
}

export default App;