import React from 'react';
import { Link } from 'react-router-dom';

class Hompage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {}
  }

  render() {
    return (
      <div>
        <h2>Paths:</h2>
        <div><Link to="/locations">Locations</Link></div>
        <div><Link to="/employee">Employee</Link></div>
        <div><Link to="/inventory">Inventory</Link></div>
        <div><Link to="/sales">Sales</Link></div>
        <div><Link to="/customers">Customers</Link></div>
        <div><Link to="/transfers">Transfers</Link></div>
        <div><Link to="/includes">Includes</Link></div>
        <div><Link to="/has">Has</Link></div>
        <div><Link to="/buys">Buys</Link></div>
        {/* Removed Owns table bc it was redundant <div><Link to="/owns">Owns</Link></div> */}
        <div><Link to="/newsale">Log a New Sale</Link></div>

        <h2>Reports:</h2>
        <div><Link to="/reports/transfers">Get a Transfers Report</Link></div>
      </div>
    );
  }
}

export default Hompage;
