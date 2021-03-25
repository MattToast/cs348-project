import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

class Locations extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      locationList: []
    }
  }

  componentDidMount() {
    fetch('/api/locations')
      .then(res => res.json())
      .then(data => this.setState({ locationList: data }));
  }

  render() {
    const locs = this.state.locationList;
    return (
      <div>
        {
          locs.map((loc) => {
            return (<ObjectCard data={loc}/>);
          })
        }
      </div>
    );
  }
}

export default Locations;
