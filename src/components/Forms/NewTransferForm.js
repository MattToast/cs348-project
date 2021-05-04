import React from 'react';

class NewTransferForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: 0,
      fromID: 0,
      toID: 0,
      amnt: 0,
    };
  }

  handleIDChange = e => this.setState({ id: e.target.value });
  handleFromIDChange = e => this.setState({ fromID: e.target.value });
  handleToIDChange = e => this.setState({ toID: e.target.value });
  handleAmountChange = e => this.setState({ amnt: e.target.value });
  handleSubmit = async e => {
    e.preventDefault();
    const res = await fetch("/api/transfers", {
      method: "POST",
      body: JSON.stringify(this.state)
    });
    if (res.ok) {
      window.location.reload();
    } else {
      window.location.href = "/error"
    }
  };

  render() {
    const s = this.state;
    return (
      <div>
        Add New Transfer:
        <form onSubmit={this.handleSubmit}>
          <div>
            <label>Transfer ID</label>
            <input type="number" value={s.id} onChange={this.handleIDChange} />
          </div>
          <div>
            <label>From ID</label>
            <input type="number" value={s.fromID} onChange={this.handleFromIDChange} />
          </div>
          <div>
            <label>To ID</label>
            <input type="number" value={s.toID} onChange={this.handleToIDChange} />
          </div>
          <div>
            <label>Amount</label>
            <input type="number" value={s.amnt} onChange={this.handleAmountChange} />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}


export default NewTransferForm;
