import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';
import NewEmployeeForm from '../components/Forms/NewEmployeeForm';

class Employees extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      employeeList: []
    }
  }

  componentDidMount() {
    fetch('/api/employees')
      .then(res => res.json())
      .then(data => this.setState({ employeeList: data }));
  }

  render() {
    const emps = this.state.employeeList;
    return (
      <div>
        <NewEmployeeForm />
        <div>
          {
            emps.map((emp) => {
              return (<ObjectCard data={emp} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Employees;
