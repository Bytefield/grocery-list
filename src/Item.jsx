import React from 'react';

export const Item = React.memo(({ feature, featureTags, background, scenario, scenarioTags, step, description, handleRemoveItem }) => {
    return (
        <li className="list_item">
            <div className="item_container">
                <p className="name">Feature Tags: {featureTags.join(', ')}</p>
                <p className="name">Feature: {feature}</p>
                <p className="name">Background: {background}</p>
                <p className="name">Scenario Tags: {scenarioTags.join(', ')}</p>
                <p className="name">Scenario: {scenario}</p>
                <p className="name">Step: {step}</p>
            </div>
            <div className="button-bar">
                <button type="button" onClick={handleRemoveItem}>Delete</button>
            </div>
        </li>
    );
});