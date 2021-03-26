import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

class Includes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      includeList: []
    }
  }

  componentDidMount() {
    fetch('/api/includes')
      .then(res => res.json())
      .then(data => this.setState({ includeList: data }));
  }

  render() {
    const incls = this.state.includeList;
    return (
      <div>
        <div>
          TODO - Adding should be handled automatically by the made sale page
        </div>
        <div>
          {
            incls.map((incl) => {
              return (<ObjectCard data={incl} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Includes;
