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
        <div><Link to="/newtransfer">Log a New Transfer</Link></div>

        <h2>Reports:</h2>
        <div><Link to="/reports/transfers">Get a Transfers Report</Link></div>
        <div><Link to={`/reports/empsales?s=${Date.now() - (1000 * 60 * 60 * 24)}&t=Report for Last Day`}>Get a Employee Sales Report For Last Day</Link></div>
        <div><Link to={`/reports/empsales?s=${Date.now() - (1000 * 60 * 60 * 24 * 7)}&t=Report for Last Week`}>Get a Employee Sales Report For Last 7 Days</Link></div>
        <div><Link to={`/reports/empsales?s=${Date.now() - (1000 * 60 * 60 * 24 * 30)}&t=Report for Last Month`}>Get a Employee Sales Report For Last 30 Days</Link></div>
        <div><Link to={`/reports/empsales?s=${Date.now() - (1000 * 60 * 60 * 24 * 365)}&t=Report for Last Year`}>Get a Employee Sales Report For Last 365 Days</Link></div>
        <div><Link to="/reports/empsales?s=0">Get a Employee Sales Report For All Time</Link></div>
        <div><Link to="/reports/moneyflow">Get a Money Flow Report</Link></div>
        <div><Link to="/reports/complex">Get a Complex Report</Link></div>
      </div>
    );
  }
}

export default Hompage;
