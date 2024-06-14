export function Item(props) {
    return (
        <li>
            <div className="container">
                <input type="checkbox" name="" id="" />
                <p>{props.value}</p>
            </div>
            <div>
                <button
                    type="button"
                    onClick={props.handleRemoveItem}
                >Button</button>
            </div>
        </li>
    );
}
