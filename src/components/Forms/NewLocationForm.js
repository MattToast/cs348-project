import React from 'react';

class NewLocationForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: 0,
      money: 0,
      owner: 0,
    };
  }

  handleIDChange = e => this.setState({ id: e.target.value });
  handleMoneyChange = e => this.setState({ money: e.target.value });
  handleOwnerChange = e => this.setState({ owner: e.target.value });
  handleSubmit = e => {
    fetch("/api/locations", {
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
        Add New Location:
        <form onSubmit={this.handleSubmit}>
          <div>
            <label>Location ID</label>
            <input type="number" value={s.id} onChange={this.handleIDChange} />
          </div>
          <div>
            <label>Money</label>
            <input type="number" value={s.money} onChange={this.handleMoneyChange} />
          </div>
          <div>
            <label>Owner ID</label>
            <input type="number" value={s.owner} onChange={this.handleOwnerChange} />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default NewLocationForm;