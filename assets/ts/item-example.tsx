import React, { useState, useEffect } from 'react';

function ItemExample() {
  const [items, setItems] = useState<{ id: number; name: string }[]>([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    fetch('/api/item/')
      .then(res => res.json())
      .then(data => setItems(data));
  }, []);

  const addItem = () => {
    fetch('/api/item/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: input })
    }).then(res => res.json())
      .then(({ item }) => {
        setItems(prev => [...prev, item]);
        setInput('');
      });
  };

  return (
    <div>
      <div className="input-field">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Add new item"
        />
      </div>
      <button className="btn" onClick={addItem}>Add</button>
      <ul className="collection">
        {items.map((item) => (
          <li key={item.id} className="collection-item">
            {item.name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ItemExample;
