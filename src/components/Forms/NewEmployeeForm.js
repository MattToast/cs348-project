import React from 'react';

class NewEmployeeForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: 0,
      position: "",
      salary: 0,
      location_id: 0
    };
  }

  handleIDChange = e => this.setState({ id: e.target.value });
  handlePosChange = e => this.setState({ position: e.target.value });
  handleSalChange = e => this.setState({ salary: e.target.value });
  handleLocChange = e => this.setState({ location_id: e.target.value });
  handleSubmit = e => {
    fetch("/api/employees", {
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
        Add New Employee:
        <form onSubmit={this.handleSubmit}>
          <div>
            <label>Employee ID</label>
            <input type="number" value={s.id} onChange={this.handleIDChange} />
          </div>
          <div>
            <label>Position</label>
            <input type="text" value={s.position} onChange={this.handlePosChange} />
          </div>
          <div>
            <label>Salary</label>
            <input type="number" value={s.salary} onChange={this.handleSalChange} />
          </div>
          <div>
            <label>Location ID</label>
            <input type="number" value={s.location_id} onChange={this.handleLocChange} />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default NewEmployeeForm;