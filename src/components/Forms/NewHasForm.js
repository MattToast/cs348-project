import React from 'react';

class NewHasForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      locID: 0,
      prodID: 0,
      price: 0,
      stock: 0,
    };
  }

  handleLocIDChange = e => this.setState({ locID: e.target.value });
  handleProdIDChange = e => this.setState({ prodID: e.target.value });
  handlePriceChange = e => this.setState({ price: e.target.value });
  handleStockChange = e => this.setState({ stock: e.target.value });
  handleSubmit = async e => {
    e.preventDefault();
    const res = await fetch("/api/has", {
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
        Add New Has:
        <form onSubmit={this.handleSubmit}>
          <div>
            <label>Location ID</label>
            <input type="number" value={s.id} onChange={this.handleLocIDChange} />
          </div>
          <div>
            <label>Product ID</label>
            <input type="number" value={s.fromID} onChange={this.handleProdIDChange} />
          </div>
          <div>
            <label>Price</label>
            <input type="number" value={s.toID} onChange={this.handlePriceChange} />
          </div>
          <div>
            <label>Stock</label>
            <input type="number" value={s.amnt} onChange={this.handleStockChange} />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}


export default NewHasForm;
