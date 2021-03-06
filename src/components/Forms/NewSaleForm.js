import React from 'react';

class NewSaleForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      saleID: 0,
      custID: 0,
      emplID: 0,
      prodID: 0,
      num: 0,
      date: ""
    };
  }

  componentDidMount() {
    const now = new Date();
    const date = `${now.getFullYear()}-${now.getMonth() + 1}-${now.getDate()}`
    this.setState({
      saleID: Date.now(),
      date
    });
  }

  handleCustIDChange = e => this.setState({ custID: e.target.value });
  handleEmpIDChange = e => this.setState({ emplID: e.target.value });
  handleProdIDChange = e => this.setState({ prodID: e.target.value });
  handleNumChange = e => this.setState({ num: e.target.value });
  handleSubmit = async e => {
    e.preventDefault();
    const res = await fetch("/api/sales", {
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
        <form onSubmit={this.handleSubmit}>
          <div>
            <span>Sale ID: {s.saleID}</span>
          </div>
          <div>
            <label>Customer ID</label>
            <input type="number" min={0} step={1} value={s.custID} onChange={this.handleCustIDChange} />
          </div>
          <div>
            <label>Employee ID</label>
            <input type="number" min={0} step={1} value={s.emplID} onChange={this.handleEmpIDChange} />
          </div>
          <div>
            <label>Product ID</label>
            <input type="number" min={0} step={1} value={s.prodID} onChange={this.handleProdIDChange} />
          </div>
          <div>
            <label>Quantiy Bought</label>
            <input type="number" min={0} step={1} value={s.num} onChange={this.handleNumChange} />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default NewSaleForm;