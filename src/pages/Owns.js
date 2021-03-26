import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

class Owns extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      ownsList: []
    }
  }

  componentDidMount() {
    fetch('/api/owns')
      .then(res => res.json())
      .then(data => this.setState({ ownsList: data }));
  }

  render() {
    const ownses = this.state.ownsList;
    return (
      <div>
        <div>
          TODO - Adding should be handled when creating a new location
        </div>
        <div>
          {
            ownses.map((own) => {
              return (<ObjectCard data={own} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Owns;
