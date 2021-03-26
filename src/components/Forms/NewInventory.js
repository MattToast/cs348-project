import React from 'react';

class NewEmployeeForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: 0,
      name: "",
    };
  }

  handleIDChange = e => this.setState({ id: e.target.value });
  handlePosChange = e => this.setState({ name: e.target.value });
  handleSubmit = e => {
    fetch("/api/inventory", {
      method: "POST",
      body: JSON.stringify(this.state)
    })
      .then(() => window.location.reload());
    e.preventDefault();
  };

  render() {
    const s = this.state;
    return (
      <div>
        Add New Inventory:
        <form onSubmit={this.handleSubmit}>
          <div>
            <label>Product ID</label>
            <input type="number" value={s.id} onChange={this.handleIDChange} />
          </div>
          <div>
            <label>Name</label>
            <input type="text" value={s.name} onChange={this.handlePosChange} />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default NewEmployeeForm;